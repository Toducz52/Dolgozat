# from PySide2.QtGui import QTextCursor
# from PySide2.QtWidgets import QPlainTextEdit
# from PySide2.QtCore import QObject, Slot, SIGNAL, Signal, qDebug
# from util.util_code_generator import *
# from util.util_regex import *
# from code_editor.qMyPushButton import *
#
#
# class MyQPlainTextEdit(QPlainTextEdit):
#     mysignal = None
#
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.prev_text_size = 0
#         self.prev_text = self.toPlainText()
#         self.setUndoRedoEnabled(True)
#         self.cannot_be_edited_interval = []
#         self.setReadOnly(True)
#         self.signal_not_work = False
#
#
#     @Slot()
#     def code_text_change_is_available(self):
#         self.setPlainText(self.prev_text)
#         QObject.connect(self, SIGNAL('textChanged()'), self.in_code_text_changed, Qt.UniqueConnection)
#         self.setReadOnly(False)
#
#     def format(self, text):
#         pos = self.textCursor().position()
#
#         prev_text = text[:pos - 1]
#         next_text = text[pos:]
#
#         if text[pos - 1] == '\t':
#             new = prev_text + '    ' + next_text
#             self.signal_not_work = True
#             self.setPlainText(new)
#             self.signal_not_work = False
#             for i in range(0, pos + 3):
#                 self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#             index = 1
#             for (start, end, check_able) in [] if len(self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
#                 if pos < start:
#                     self.cannot_be_edited_interval[index] = [start + 3, end + 3, check_able]
#                 index += 1
#             self.prev_text = self.toPlainText()
#             self.prev_text_size = len(self.prev_text)
#
#         if text[pos - 1] == ':':
#             self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
#             pos_temp = self.textCursor().position()
#             space_number = 0
#             while pos_temp < pos and text[pos_temp] == ' ':
#                 space_number = space_number + 1
#                 pos_temp = pos_temp + 1
#             center = ''
#             for index in range(0, space_number + 4):
#                 center = center + ' '
#             new = prev_text + ':\n' + center + next_text
#             self.signal_not_work = True
#             self.setPlainText(new)
#             self.signal_not_work = False
#             for i in range(0, pos + 1 + len(center)):
#                 self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#             index = 1
#             for (start, end, check_able) in [] if len(self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
#                 if pos < start:
#                     self.cannot_be_edited_interval[index] = [start + 1 + len(center), end + 1 + len(center), check_able]
#                 index += 1
#             self.prev_text = self.toPlainText()
#             self.prev_text_size = len(self.prev_text)
#
#         if text[:-1].find('\n') > 0:
#             if text[pos - 1] == '\n':
#                 save = self.textCursor()
#                 self.moveCursor(QTextCursor.Up, QTextCursor.MoveAnchor)
#                 self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
#                 pos_temp = self.textCursor().position()
#                 space_number = 0
#                 while pos_temp < pos and text[pos_temp] == ' ':
#                     space_number = space_number + 1
#                     pos_temp = pos_temp + 1
#                 center = ''
#                 if space_number > 0:
#                     for index in range(0, space_number):
#                         center = center + ' '
#                     new = prev_text + '\n' + center + next_text
#                     self.signal_not_work = True
#                     self.setPlainText(new)
#                     self.signal_not_work = False
#                     index = 1
#                     for (start, end, check_able) in [] if len(
#                             self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
#                         if pos < start:
#                             self.cannot_be_edited_interval[index] = [start + len(center), end + len(center), check_able]
#                         index += 1
#                     for i in range(0, pos + len(center)):
#                         self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#                     self.prev_text = self.toPlainText()
#                     self.prev_text_size = len(self.prev_text)
#                 else:
#                     self.setTextCursor(save)
#
#     @Slot()
#     def in_code_text_changed(self):
#
#         if self.signal_not_work:
#             return None
#
#         self.setReadOnly(True)
#
#         pos_temp = self.textCursor().position()
#
#         text = self.toPlainText()
#
#         if len(text) > self.prev_text_size:
#
#             difference = len(text) - self.prev_text_size
#             index = 0
#             for (start, end, check_able) in self.cannot_be_edited_interval:
#                 if check_able and start <= pos_temp - difference < end:
#                     self.signal_not_work = True
#                     self.setPlainText(self.prev_text)
#                     self.signal_not_work = False
#                     for i in range(0, pos_temp - difference):
#                         self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#                     self.setReadOnly(False)
#                     return None
#                 else:
#                     if start > pos_temp - difference and index != 0:
#                         self.cannot_be_edited_interval[index] = [start + difference, end + difference, check_able]
#                 index += 1
#
#             self.format(text)
#
#         else:
#             difference = self.prev_text_size - len(text)
#             index = 0
#             for (start, end, check_able) in self.cannot_be_edited_interval:
#
#                 if check_able and pos_temp < end and pos_temp + difference >= start:
#                     self.signal_not_work = True
#                     self.setPlainText(self.prev_text)
#                     self.signal_not_work = False
#                     for i in range(0, pos_temp):
#                         self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#                     self.setReadOnly(False)
#                     return None
#                 else:
#                     if start > pos_temp + difference and index != 0:
#                         self.cannot_be_edited_interval[index] = [start - difference, end - difference, check_able]
#                 index += 1
#
#             try:
#                 if self.prev_text[pos_temp] == ' ':
#                     if self.prev_text[pos_temp - 1] == ' ' and self.prev_text[pos_temp - 2] == ' ' and \
#                             self.prev_text[pos_temp - 3] == ' ':
#                         prev_text = self.prev_text[:pos_temp - 3]
#                         next_text = self.prev_text[pos_temp + 1:]
#                         new = prev_text + next_text
#                         self.signal_not_work = True
#                         self.setPlainText(new)
#                         self.signal_not_work = False
#                         for i in range(0, pos_temp - 3):
#                             self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#                         index = 1
#                         for (start, end, check_able) in [] if len(
#                                 self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
#                             if pos_temp <= start:
#                                 self.cannot_be_edited_interval[index] = [start - 3, end - 3, check_able]
#                             index += 1
#
#             except:
#                 pass
#
#         self.prev_text_size = len(self.toPlainText())
#         self.prev_text = self.toPlainText()
#
#         self.setReadOnly(False)
#
#     @Slot()
#     def add_cannot_be_edited_interval(self, start, end, row):
#         print('cannot: ' + str(self.cannot_be_edited_interval))
#         try:
#             self.cannot_be_edited_interval[row + 1] = [start, end, True]
#         except IndexError:
#             self.cannot_be_edited_interval.append([start, end, True])
#         print('cannot: ' + str(self.cannot_be_edited_interval))
#
#     def delete_function_call_to_code(self, row):
#
#         print('delete: ' + str(self.cannot_be_edited_interval) + ' --> ' + str(row))
#
#         start, finish, check_able = self.cannot_be_edited_interval[row + 1]
#         self.cannot_be_edited_interval[row + 1] = [start, finish, False]
#
#         text = self.toPlainText()
#
#         prev_text = text[:start - 1]
#         next_text = text[finish:]
#         new_text = prev_text + next_text
#
#         self.signal_not_work = True
#         self.setPlainText(new_text)
#         self.signal_not_work = False
#
#         for i in range(0, len(new_text)):
#             self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#
#         self.prev_text = self.toPlainText()
#         self.prev_text_size = len(self.toPlainText())
#
#         difference = finish - start
#
#         index = 1
#         for (start1, end1, check_able1) in self.cannot_be_edited_interval[1:]:
#             if finish < start1:
#                 self.cannot_be_edited_interval[index] = [start1 - difference - 1, end1 -
#                                                          difference - 1, check_able1]
#             index += 1
#
#         print('delete: ' + str(self.cannot_be_edited_interval))
#
#     def add_function_call_to_code(self, function_call, row):
#
#         print('add: ' + str(self.cannot_be_edited_interval))
#
#         v1 = function_call.v1
#         v2 = function_call.v2
#         prop = function_call.prop
#
#         if len(self.cannot_be_edited_interval) == 0:
#             # return -1, ha meg a fejlec nincs beallitva
#             raise Exception('A fejléc nincs beállítva')
#
#         text_cursor_pos = self.textCursor().position()
#
#         text = self.toPlainText()
#
#         prev_text = text[:text_cursor_pos]
#         next_text = text[text_cursor_pos:]
#
#         new_line = create_new_line(prop, v1, v2)
#
#         new = prev_text + new_line + next_text
#
#         for (start, end, check_able) in self.cannot_be_edited_interval:
#             if check_able and start <= text_cursor_pos <= end:
#                 # return -2, ha olyan helyre akartam beszurni, ami mar beszurt hely
#                 raise Exception('Erre a pozicíóra nem lehet beszurni.')
#
#         index = 1
#         for (start, end, check_able) in self.cannot_be_edited_interval[1:]:
#             if start >= text_cursor_pos:
#                 self.cannot_be_edited_interval[index] = [start + len(new_line), end + len(new_line), check_able]
#
#         self.signal_not_work = True
#         self.setPlainText(new)
#         self.signal_not_work = False
#
#         self.add_cannot_be_edited_interval(text_cursor_pos + 1, text_cursor_pos + len(new_line), row)
#
#         for i in range(0, text_cursor_pos + len(new_line)):
#             self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#
#         self.prev_text = self.toPlainText()
#         self.prev_text_size = len(self.prev_text)
#
#         print('add: ' + str(self.cannot_be_edited_interval))
#
#         return text_cursor_pos + 1, text_cursor_pos + len(new_line)
#
#     def add_function_head_to_code(self, function_name, parameter_list):
#
#         parameters = ''
#         for p in parameter_list:
#             parameters += p + ','
#         parameters = parameters[:-1]
#
#         header = f"def {function_name}({parameters}):\n"
#
#         text = self.toPlainText()
#
#         prev_header = first_match(text,
#                                   "\s*def\s+[a-zA-Z][a-zA-Z0-9]+\s*\(([a-zA-z][a-zA-z0-9]*,\s*)*([a-zA-z][a-zA-z0-9]*)\):\n")
#
#         code_definition = ""
#         difference = 0
#
#         print('--' + str(self.cannot_be_edited_interval))
#
#         if prev_header is not None:
#             difference = len(header) - len(prev_header)
#
#             index = 1
#             for (start, end, check_able) in self.cannot_be_edited_interval[1:]:
#                 self.cannot_be_edited_interval[index] = [start + difference, end + difference, check_able]
#                 index += 1
#             code_definition = text[len(prev_header):]
#
#         self.cannot_be_edited_interval = [(0, len(header), True)] + self.cannot_be_edited_interval[1:]
#
#         print(str(self.cannot_be_edited_interval))
#
#         new_code = header + code_definition
#
#         self.signal_not_work = True
#         self.setPlainText(new_code)
#         self.signal_not_work = False
#
#         self.prev_text = self.toPlainText()
#         self.prev_text_size = len(self.prev_text)
#
#         for i in range(0, len(header) + 1):
#             self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
#
#         return header
#
#     def load_cannot_be_edited_interval(self, function_call):
#
#         self.cannot_be_edited_interval = self.cannot_be_edited_interval[:1]
#
#         for call in function_call:
#             self.cannot_be_edited_interval.append([call.start, call.end, True])


from PySide2.QtCore import Slot, Qt, QRect, QSize, QObject, SIGNAL
from PySide2.QtGui import QColor, QPainter, QTextFormat, QTextCursor
from PySide2.QtWidgets import QPlainTextEdit, QWidget, QTextEdit

from util.util_code_generator import *
from util.util_regex import *


class LineNumberArea(QWidget):
    def __init__(self, editor):
        QWidget.__init__(self, editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class MyQPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent):
        QPlainTextEdit.__init__(self)
        self.line_number_area = LineNumberArea(self)

        self.blockCountChanged[int].connect(self.update_line_number_area_width)
        self.updateRequest[QRect, int].connect(self.update_line_number_area)
        self.cursorPositionChanged.connect(self.highlight_current_line)

        self.update_line_number_area_width(0)
        self.highlight_current_line()

        # QObject.connect(self, SIGNAL('textChanged()'), self.in_code_text_changed, Qt.UniqueConnection)

        self.prev_text_size = 0
        self.prev_text = self.toPlainText()
        self.setUndoRedoEnabled(True)
        self.cannot_be_edited_interval = []
        self.setReadOnly(True)
        self.signal_not_work = False

    def clearValue(self):
        self.prev_text_size = 0
        self.prev_text = self.toPlainText()
        self.cannot_be_edited_interval = []


    def line_number_area_width(self):
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num *= 0.1
            digits += 1

        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def resizeEvent(self, e):
        super().resizeEvent(e)
        cr = self.contentsRect()
        width = self.line_number_area_width()
        rect = QRect(cr.left(), cr.top(), width, cr.height())
        self.line_number_area.setGeometry(rect)

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), Qt.lightGray)
        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        offset = self.contentOffset()
        top = self.blockBoundingGeometry(block).translated(offset).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                width = self.line_number_area.width()
                height = self.fontMetrics().height()
                painter.drawText(0, top, width, height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    @Slot()
    def update_line_number_area_width(self, newBlockCount):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    @Slot()
    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            width = self.line_number_area.width()
            self.line_number_area.update(0, rect.y(), width, rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    @Slot()
    def highlight_current_line(self):
        extra_selections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()

            line_color = QColor(Qt.yellow).lighter(160)
            selection.format.setBackground(line_color)

            selection.format.setProperty(QTextFormat.FullWidthSelection, True)

            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()

            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    @Slot()
    def code_text_change_is_available(self):
        self.setPlainText(self.prev_text)
        QObject.connect(self, SIGNAL('textChanged()'), self.in_code_text_changed, Qt.UniqueConnection)
        self.setReadOnly(False)

    def format(self, text):
        pos = self.textCursor().position()

        prev_text = text[:pos - 1]
        next_text = text[pos:]

        if text[pos - 1] == '\t':
            new = prev_text + '    ' + next_text
            self.signal_not_work = True
            self.setPlainText(new)
            self.signal_not_work = False
            for i in range(0, pos + 3):
                self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
            index = 1
            for (start, end, check_able) in [] if len(
                    self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
                if pos < start:
                    self.cannot_be_edited_interval[index] = [start + 3, end + 3, check_able]
                index += 1
            self.prev_text = self.toPlainText()
            self.prev_text_size = len(self.prev_text)

        if text[pos - 1] == ':':
            self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
            pos_temp = self.textCursor().position()
            space_number = 0
            while pos_temp < pos and text[pos_temp] == ' ':
                space_number = space_number + 1
                pos_temp = pos_temp + 1
            center = ''
            for index in range(0, space_number + 4):
                center = center + ' '
            new = prev_text + ':\n' + center + next_text
            self.signal_not_work = True
            self.setPlainText(new)
            self.signal_not_work = False
            for i in range(0, pos + 1 + len(center)):
                self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
            index = 1
            for (start, end, check_able) in [] if len(
                    self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
                if pos < start:
                    self.cannot_be_edited_interval[index] = [start + 1 + len(center), end + 1 + len(center), check_able]
                index += 1
            self.prev_text = self.toPlainText()
            self.prev_text_size = len(self.prev_text)

        if text[:-1].find('\n') > 0:
            if text[pos - 1] == '\n':
                save = self.textCursor()
                self.moveCursor(QTextCursor.Up, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                pos_temp = self.textCursor().position()
                space_number = 0
                while pos_temp < pos and text[pos_temp] == ' ':
                    space_number = space_number + 1
                    pos_temp = pos_temp + 1
                center = ''
                if space_number > 0:
                    for index in range(0, space_number):
                        center = center + ' '
                    new = prev_text + '\n' + center + next_text
                    self.signal_not_work = True
                    self.setPlainText(new)
                    self.signal_not_work = False
                    index = 1
                    for (start, end, check_able) in [] if len(
                            self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
                        if pos < start:
                            self.cannot_be_edited_interval[index] = [start + len(center), end + len(center), check_able]
                        index += 1
                    for i in range(0, pos + len(center)):
                        self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
                    self.prev_text = self.toPlainText()
                    self.prev_text_size = len(self.prev_text)
                else:
                    self.setTextCursor(save)

    @Slot()
    def in_code_text_changed(self):

        if self.signal_not_work:
            return None

        self.setReadOnly(True)

        pos_temp = self.textCursor().position()

        text = self.toPlainText()

        if len(text) > self.prev_text_size:

            difference = len(text) - self.prev_text_size
            index = 0
            for (start, end, check_able) in self.cannot_be_edited_interval:
                if check_able and start <= pos_temp - difference < end:
                    self.signal_not_work = True
                    self.setPlainText(self.prev_text)
                    self.signal_not_work = False
                    for i in range(0, pos_temp - difference):
                        self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
                    self.setReadOnly(False)
                    return None
                else:
                    if start > pos_temp - difference and index != 0:
                        self.cannot_be_edited_interval[index] = [start + difference, end + difference, check_able]
                index += 1

            self.format(text)

        else:
            difference = self.prev_text_size - len(text)
            index = 0
            for (start, end, check_able) in self.cannot_be_edited_interval:
                print(start)
                print(end)
                print(check_able)
                if check_able and pos_temp < end and pos_temp + difference >= start:
                    self.signal_not_work = True
                    self.setPlainText(self.prev_text)
                    self.signal_not_work = False
                    for i in range(0, pos_temp):
                        self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
                    self.setReadOnly(False)
                    return None
                else:
                    if start > pos_temp + difference and index != 0:
                        self.cannot_be_edited_interval[index] = [start - difference, end - difference, check_able]
                index += 1

            try:
                if self.prev_text[pos_temp] == ' ':
                    if self.prev_text[pos_temp - 1] == ' ' and self.prev_text[pos_temp - 2] == ' ' and \
                            self.prev_text[pos_temp - 3] == ' ':
                        prev_text = self.prev_text[:pos_temp - 3]
                        next_text = self.prev_text[pos_temp + 1:]
                        new = prev_text + next_text
                        self.signal_not_work = True
                        self.setPlainText(new)
                        self.signal_not_work = False
                        for i in range(0, pos_temp - 3):
                            self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)
                        index = 1
                        for (start, end, check_able) in [] if len(
                                self.cannot_be_edited_interval) == 0 else self.cannot_be_edited_interval[1:]:
                            if pos_temp <= start:
                                self.cannot_be_edited_interval[index] = [start - 3, end - 3, check_able]
                            index += 1

            except:
                pass

        self.prev_text_size = len(self.toPlainText())
        self.prev_text = self.toPlainText()

        self.setReadOnly(False)

    @Slot()
    def add_cannot_be_edited_interval(self, start, end, row):
        # print('cannot: ' + str(self.cannot_be_edited_interval))
        try:
            self.cannot_be_edited_interval[row + 1] = [start, end, True]
        except IndexError:
            self.cannot_be_edited_interval.append([start, end, True])
        # print('cannot: ' + str(self.cannot_be_edited_interval))

    def delete_function_call_to_code(self, row):

        # print('delete: ' + str(self.cannot_be_edited_interval) + ' --> ' + str(row))

        start, finish, check_able = self.cannot_be_edited_interval[row + 1]
        self.cannot_be_edited_interval[row + 1] = [start, finish, False]

        text = self.toPlainText()

        prev_text = text[:start - 1]
        next_text = text[finish:]
        new_text = prev_text + next_text

        self.signal_not_work = True
        self.setPlainText(new_text)
        self.signal_not_work = False

        for i in range(0, len(new_text)):
            self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)

        self.prev_text = self.toPlainText()
        self.prev_text_size = len(self.toPlainText())

        difference = finish - start

        index = 1
        for (start1, end1, check_able1) in self.cannot_be_edited_interval[1:]:
            if finish < start1:
                self.cannot_be_edited_interval[index] = [start1 - difference - 1, end1 -
                                                         difference - 1, check_able1]
            index += 1

        # print('delete: ' + str(self.cannot_be_edited_interval))

    def add_function_call_to_code(self, function_call, row):

        # print('add: ' + str(self.cannot_be_edited_interval))

        v1 = function_call.v1
        v2 = function_call.v2
        prop = function_call.prop

        if len(self.cannot_be_edited_interval) == 0:
            # return -1, ha meg a fejlec nincs beallitva
            raise Exception('A fejléc nincs beállítva')

        text_cursor_pos = self.textCursor().position()

        text = self.toPlainText()

        prev_text = text[:text_cursor_pos]
        next_text = text[text_cursor_pos:]

        new_line = create_new_line(v1, v2, prop)

        new = prev_text + new_line + next_text

        for (start, end, check_able) in self.cannot_be_edited_interval:
            if check_able and start <= text_cursor_pos <= end:
                # return -2, ha olyan helyre akartam beszurni, ami mar beszurt hely
                raise Exception('Erre a pozicíóra nem lehet beszurni.')

        index = 1
        for (start, end, check_able) in self.cannot_be_edited_interval[1:]:
            if start >= text_cursor_pos:
                self.cannot_be_edited_interval[index] = [start + len(new_line), end + len(new_line), check_able]

        self.signal_not_work = True
        self.setPlainText(new)
        self.signal_not_work = False

        self.add_cannot_be_edited_interval(text_cursor_pos + 1, text_cursor_pos + len(new_line), row)

        for i in range(0, text_cursor_pos + len(new_line)):
            self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)

        self.prev_text = self.toPlainText()
        self.prev_text_size = len(self.prev_text)

        # print('add: ' + str(self.cannot_be_edited_interval))

        return text_cursor_pos + 1, text_cursor_pos + len(new_line)

    def add_function_head_to_code(self, function_name, parameter_list):

        parameters = ''
        for p in parameter_list:
            parameters += p + ','
        parameters = parameters[:-1]

        header = f"def {function_name}({parameters}):\n"

        text = self.toPlainText()

        prev_header = first_match(text,
                                  "\s*def\s+[a-zA-Z][a-zA-Z0-9]+\s*\(([a-zA-z][a-zA-z0-9]*,\s*)*([a-zA-z][a-zA-z0-9]*)\):\n")

        code_definition = ""
        difference = 0

        # print('--' + str(self.cannot_be_edited_interval))

        if prev_header is not None:
            difference = len(header) - len(prev_header)

            index = 1
            for (start, end, check_able) in self.cannot_be_edited_interval[1:]:
                self.cannot_be_edited_interval[index] = [start + difference, end + difference, check_able]
                index += 1
            code_definition = text[len(prev_header):]

        self.cannot_be_edited_interval = [(0, len(header), True)] + self.cannot_be_edited_interval[1:]

        # print(str(self.cannot_be_edited_interval))

        new_code = header + code_definition

        self.signal_not_work = True
        self.setPlainText(new_code)
        self.signal_not_work = False

        self.prev_text = self.toPlainText()
        self.prev_text_size = len(self.prev_text)

        for i in range(0, len(header) + 1):
            self.moveCursor(QTextCursor.MoveOperation.Right, QTextCursor.MoveAnchor)

        return header

    def load_cannot_be_edited_interval(self, function_call):

        self.cannot_be_edited_interval = self.cannot_be_edited_interval[:1]

        for call in function_call:
            self.cannot_be_edited_interval.append([call.start, call.end, True])

