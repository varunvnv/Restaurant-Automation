
Models
======
THIS IS THE DOCUMENTATION PAGE FOR OUR MODELS

**class Employee(models.Model):**
********************************************
The class Employee is used to give the static view of the employees 
working for the restaurant.
The attributes of the class Employee are:
1) username: The attribute username is of type string. Each employee would 
   have a unique username to be able to Login to the site.
2) password: The attribute password is of type string. Each employee would 
   have a unique password to be able to Login to the site.
   The combination of the username and password should also be unique to 
   each employee.
3) role: The attribute role is of type integer. It is used to identify the 
   role of an employee. The roles that are currently in the restaurant are:
   a) Manager: The unique code of Manager is 01. A manager can recruit 
               employees, asign shifts to them and manage menu items.
   b) Chef: The unique code of Chef is 02. A chef can view all the orders 
            and change the status of the order from Active (01) to 
			Process (02) and from Process to Done(03).
   c) Waiter: The unique code of Waiter is 03. A waiter can see his tables
              alloted to him by the manager and place orders for each table.
              He can also change the status from Clean (01) to Dirty (02)
   d) Host/Hostess: The unique code of Host/Hostess is 04. A Host/Hostess can 
              see the tables that are Free (01) to occupied (02).
   e) Busboy: The unique code of Busboy is 05. A Busboy can view the tables 
              that are Dirty(02) to Clean (01) after cleaning them.
			  
			  
**class Table(models.Model):**
********************************************
The class Table is used to give the static view of the tables present in
the restaurant.
The attributes of the class Employee are:
1) employee_id: It is the Foreign key from table Employee which is of type
                integer and is used to assign each unique table to unique employee.
				Here both of these tables are associated with many to one 
				relationship. 
				
**class Item(models.Model):**
********************************************
The class Item is used to give the static view of the items in the menu.
The attributes of the class Item are:
1) name: The attribute name is of type string and is used to identify the item.
         Each item name is unique.
2) price: The attribute price is of type double and is used to give the price
          of the item. the manager can change the price of the item at any time.
3) type: The attribute type is of type string and is used to describe in what 
         category the item falls under. The type is a unique attribute.
		 
**class Order(models.Model):**
********************************************
The class Order is used to give the static view of the order placed by a table.
The attributes of the class Order are:
1) employee_id: The attribute employee_id is a Foreign key from the table employee
   to know by which employee is the order placed.
2) table_id: The attribute table_id is a Foreign key from the table 'table' to
   have an idea of what table does the order belong to
3) status: The attribute status is of type integer and is used to keep track of the
   status of the order. Only chef has the authorization to change the status of the 
   orders placed. Various status used are:
   a) Active: Indicates that the order is not yet started cooking and is represented 
              by integer 01.
   b) Process: Indicates that the order is in process of preparation once 
               the chef selects the order from active site. It is represented by the 
			   integer 02.
   c) Done: Indicates that the order is ready to serve. The status is changed by the 
            chef once the order is cooked in order to let the wiater to know so that 
			he can serve. It is represented by the integer 03.
4) order_date: The attribute order_date is of type date and is used to keep track of 
               the date, the order was placed for future reference.
5) items: The attribute items is used to keep the list of items placed in an order 
          that are mapped from the table Item associating with many to many relationship.

		  
**class OrderItem(models.Model):**
********************************************
The class OrderItem is used to give the static view of the items placed in an order
by a table.
The attributes of the class OrderItem are:
1) order_id: The attribute order_id is used to know which item comes under what order.
             It is a Foreign key mapped from the table Order. 
2) item_id: The attribute item_id is a Foreign key mapped from the table Item to let us 
            know the items under an order.
			
**class Shift(models.Model):**
The class Shift is used to give the static view of the shifts of employees.
The attributes of the class Shift are:
1) user_id: This attribute is used to map to which user the shift is allotted to. 
            It is a Foreign key mapped from the table Users.
2) start_date: The attribute start_date is of type date and is used to give an employee's 
               start date and time of his shift.
3) end_date: The attribute end_date is of type date and is used to give an employee's 
             ending date and time of his shift.
			 
**class OrderList(models.Model):**
The class OrderList is used to give the static view of the bills that are active so that 
the waiter can see them at any time for refernce.
The attributes of the class Shift are:
1) order_id: This attribute is used to track which order the list belongs to. 
             It is a Foreign key mapped from the table Order.
2) item_name: This attribute is used for displaying the items in a bill.
              It is a Foreign key mapped from the table Item. 
3) table_id: The attribute table_id is used to map to which table the order belongs to.
             It is a Foreign key mapped from the table Table.
4) status: This attribute is of type integer and is used to track whether an order is completed
           or is active.