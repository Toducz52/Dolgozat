from PySide2.QtWidgets import QMessageBox


def create_simple_message_box_and_run(self, text):

    msg_box = QMessageBox(self)
    msg_box.setText(text)
    msg_box.exec_()


def create_detail_message_box(self, text, detaile_text):
    msg_box = QMessageBox(self)
    msg_box.setText(text)
    msg_box.setInformativeText("")
    msg_box.setDetailedText(detaile_text)
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.exec_()