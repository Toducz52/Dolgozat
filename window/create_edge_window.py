from collections import Counter
from PySide2.QtWidgets import QWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QTableWidgetSelectionRange
from window.ui_py.ui_create_edge_window import Ui_Form
from PySide2.QtCore import Slot, SIGNAL, QObject, Qt
from util.util_regex import is_valid_function_name
from util.util_msg_box import create_simple_message_box_and_run
from db.DB import Function_call
import uuid


def is_valid_prop(prop):
    if prop == '' or prop is None:
        return False
    return True


def is_valid_node(node):
    if node == '' or node is None:
        return False
    if node.find('\'') >= 0:
        raise Exception(f' Nem tartalmazhatja a szöveg a következő karaktert \', használjon helyette ".')
    return True


class Create_edge_window(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.initialization_table()
        QObject.connect(self.ui.btn_add_new_row, SIGNAL("clicked()"), self.add_row_in_table)
        self.ui.btn_delete_row.clicked.connect(self.delete_row_in_table)



    @Slot()
    def previousWeek(self, row, column):
        if column == 3 and self.ui.tableWidget.item(row, 7).text() == 'active':
            self.ui.tableWidget.item(row, 7).setText('inactive')
            if not self.insert_function_call_to_code_editor(row):
                self.ui.tableWidget.item(row, 7).setText('active')

        if column == 4 and self.ui.tableWidget.item(row, 7).text() == 'inactive':
            self.ui.tableWidget.item(row, 7).setText('active')
            if not self.delete_function_call_from_code_editor(row):
                self.ui.tableWidget.item(row, 7).setText('inactive')

    def insert_function_call_to_code_editor(self, row):

        try:
            function_call = self.get_function_call(row)
            location = self.parent.ui.in_code.add_function_call_to_code(function_call, row)
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem('inactive'))
            self.ui.tableWidget.item(row, 0).setFlags(self.ui.tableWidget.item(row, 2).flags() & ~Qt.ItemIsEditable)
            self.ui.tableWidget.item(row, 1).setFlags(self.ui.tableWidget.item(row, 2).flags() & ~Qt.ItemIsEditable)
            self.ui.tableWidget.item(row, 2).setFlags(self.ui.tableWidget.item(row, 2).flags() & ~Qt.ItemIsEditable)

        except Exception as ex:
            create_simple_message_box_and_run(self, str(ex))
            return False

        return True

    def delete_function_call_from_code_editor(self, row):

        try:
            function_call = self.get_function_call(row)
            self.parent.ui.in_code.delete_function_call_to_code(row)
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem('active'))
            self.ui.tableWidget.item(row, 0).setFlags(self.ui.tableWidget.item(row, 2).flags() | Qt.ItemIsEditable)
            self.ui.tableWidget.item(row, 1).setFlags(self.ui.tableWidget.item(row, 2).flags() | Qt.ItemIsEditable)
            self.ui.tableWidget.item(row, 2).setFlags(self.ui.tableWidget.item(row, 2).flags() | Qt.ItemIsEditable)
        except Exception as ex:
            create_simple_message_box_and_run(self, str(ex))
            return False

        return True

    def initialization_table(self):
        # Row count
        self.ui.tableWidget.setRowCount(0)

        # Column count
        self.ui.tableWidget.setColumnCount(8)

        labels = ['Csomopont 1', 'Csomopont 2', 'Tartalmazó gráf', 'Hozzáad', 'Töröl', 'Start', 'End',
                  'active_start_clickable']

        self.ui.tableWidget.setHorizontalHeaderLabels(labels)

        self.ui.tableWidget.setColumnHidden(5, True)
        self.ui.tableWidget.setColumnHidden(6, True)
        self.ui.tableWidget.setColumnHidden(7, True)

        QObject.connect(self.ui.tableWidget, SIGNAL('cellClicked(int, int)'), self.previousWeek)

    def add_row_in_table(self):

        new_row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(new_row + 1)

        self.ui.tableWidget.setItem(new_row, 3, QTableWidgetItem('Hozzaad'))
        self.ui.tableWidget.setItem(new_row, 4, QTableWidgetItem('Torol'))

        self.ui.tableWidget.setItem(new_row, 7, QTableWidgetItem('active'))

        self.ui.tableWidget.item(new_row, 3).setFlags(Qt.ItemIsEnabled)
        self.ui.tableWidget.item(new_row, 4).setFlags(Qt.ItemIsEnabled)
        # self.ui.tableWidget.item(new_row, 3).setFlags(Qt.ItemIsSelectable, False)
        # self.ui.tableWidget.item(new_row, 4).setFlags(Qt.ItemIsSelectable, False)

    def delete_row_in_table(self):

        selected_row = -1

        try:
            selected_row = self.ui.tableWidget.selectionModel().selectedRows()[0].row()
        except Exception as error:
            create_simple_message_box_and_run(self, "Egyet valasszon ki.")
            return None

        if self.ui.tableWidget.item(selected_row, 7).text() == 'inactive':
            self.delete_function_call_from_code_editor(selected_row)

        try:
            del self.parent.ui.in_code.cannot_be_edited_interval[selected_row + 1]
        except:
            pass

        self.ui.tableWidget.removeRow(selected_row)

    def get_list_unique_prop(self):
        props = [prop.prop for prop in self.get_list_of_active_function_call()]
        return list(Counter(props).keys())

    def get_list_of_active_function_call(self):

        list_calls = []

        for row_index in range(0, self.ui.tableWidget.rowCount()):

            if self.ui.tableWidget.item(row_index, 7).text() == 'inactive':
                try:
                    function_call = self.get_function_call(row_index)
                    list_calls.append(function_call)
                except Exception as ex:
                    # create_simple_message_box_and_run(self, str(ex))
                    raise ex

        return list_calls

    validation_function_base_column = {
        'Csomopont 1': is_valid_node,
        'Csomopont 2': is_valid_node,
        'Tartalmazó gráf': is_valid_prop,
        'Start': str.isnumeric,
        'End': str.isnumeric
    }

    def get_function_call(self, row):

        self.ui.tableWidget.setRangeSelected(
            QTableWidgetSelectionRange(0, 0, self.ui.tableWidget.rowCount() - 1, self.ui.tableWidget.columnCount() - 1),
            False)

        selected_range = QTableWidgetSelectionRange(row, 0, row, 2)
        cells = []

        self.ui.tableWidget.setRangeSelected(selected_range, True)
        selected_items = self.ui.tableWidget.selectedItems()
        self.ui.tableWidget.setRangeSelected(selected_range, False)

        if len(selected_items) == 0:
            raise Exception("Nincs megfelelően kitöltve.")

        for selected_item in selected_items:
            column_name = self.ui.tableWidget.horizontalHeaderItem(selected_item.column()).text()
            if selected_item is None:
                raise Exception(f'{column_name}: {selected_item.row()} eleme nincs inicializálva')
            if not self.validation_function_base_column[column_name](selected_item.text()):
                raise Exception(f'{column_name}: {selected_item.row()} eleme nem megfelelő')
            cells.append(selected_item.text())

        if self.ui.tableWidget.item(row, 7).text() == 'inactive':
            try:
                start, end, check_able = self.parent.ui.in_code.cannot_be_edited_interval[row + 1]
                cells += [start, end]
            except Exception as ex:
                pass

        function_call = Function_call(*cells)

        return function_call

    def delete_all_row(self):
        for i in range(0, self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.removeRow(i)

    def load_data(self, function_call):

        self.delete_all_row()

        for row_index in range(0, len(function_call)):
            self.add_row_in_table()
            self.ui.tableWidget.setItem(row_index, 0, QTableWidgetItem(function_call[row_index].v1))
            self.ui.tableWidget.setItem(row_index, 1, QTableWidgetItem(function_call[row_index].v2))
            self.ui.tableWidget.setItem(row_index, 2, QTableWidgetItem(function_call[row_index].prop))
            self.ui.tableWidget.setItem(row_index, 7, QTableWidgetItem("inactive"))
