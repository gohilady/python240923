import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os.path

# 데이터베이스 처리를 담당하는 클래스
class ProductDatabase:
    def __init__(self, db_name="ProductList.db"):
        # DB 파일이 없으면 새로 생성, 있으면 연결
        self.db_name = db_name
        if not os.path.exists(self.db_name):
            self.create_db()
        else:
            self.con = sqlite3.connect(self.db_name)
            self.cur = self.con.cursor()

    def create_db(self):
        """데이터베이스 및 테이블을 생성하는 함수"""
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )
        self.con.commit()

    def add_product(self, name, price):
        """제품을 추가하는 함수"""
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        """제품 정보를 수정하는 함수"""
        self.cur.execute("UPDATE Products SET Name = ?, Price = ? WHERE id = ?;", (name, price, prod_id))
        self.con.commit()

    def delete_product(self, prod_id):
        """제품을 삭제하는 함수"""
        self.cur.execute("DELETE FROM Products WHERE id = ?;", (prod_id,))
        self.con.commit()

    def get_all_products(self):
        """모든 제품 정보를 반환하는 함수"""
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# UI 및 로직 처리를 담당하는 클래스
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ProductDatabase 객체 생성
        self.db = ProductDatabase()

        # UI 초기화
        self.init_ui()

        # 버튼 및 이벤트 처리 연결 (메서드 이름을 CamelCase로 변경)
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def init_ui(self):
        """UI 요소 초기화"""
        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        # 제품 목록 갱신
        self.getProducts()

    def getProducts(self):
        """DB에서 제품 목록을 가져와서 UI에 표시"""
        self.tableWidget.clearContents()
        products = self.db.get_all_products()

        # 테이블에 제품 데이터 추가
        for row, product in enumerate(products):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(product[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(product[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(product[2])))

    def addProduct(self):
        """새로운 제품을 추가"""
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.add_product(name, price)
        self.getProducts()

    def updateProduct(self):
        """선택한 제품 정보를 수정"""
        prod_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db.update_product(prod_id, name, price)
        self.getProducts()

    def removeProduct(self):
        """선택한 제품을 삭제"""
        prod_id = self.prodID.text()
        self.db.delete_product(prod_id)
        self.getProducts()

    def doubleClick(self):
        """테이블에서 더블 클릭한 제품 정보를 입력 필드에 출력"""
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 메인 실행 부분
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
