Views
======
 
THIS IS THE VIEWS DOCUMENTATION PAGE


**def access_restricted(request,users_group)**
********************************************
	 returns True if the user belongs to the group, False otherwise 

**def detail(request, emp_id)**
********************************************
	Gets the tables of every waiter and passses them as arguments to the detail.html page

**def index(request)**
********************************************
	The starting page of the placeorder app. Displays all the Users

**def menutype(request, emp_id, table_id)**
********************************************
	Gets all the menu items ordered by type and passes them as argument to the menu.html page

**def menu(request, emp_id, table_id, menu_type)**
********************************************
	Gets all the menu items that have the specifief menu type and passes them as argument to the menuitem.html

**def placeorder(request, emp_id, table_id, menu_type, menu_item)**
********************************************
	Gets the all the items that are ordered and passes them as argument to the placeorder.html file to display them and their cost.

**def placeordersuccess(request, emp_id, table_id, menu_type, random, rand)**
********************************************
	Places the final order and passes it as an argument to the orderplaced.html

**def view_active_orders(request)**
********************************************
	Gets all the active orders and passes them as an argument to the view_active_orders.html page

**def view_in_progress_orders(request)** 
********************************************
	Gets all the in progress orders and passes them as an argument to the view_in_progress_orders.html page

**def orders_detail(request, slug)**
******************************************** 
	Shows the details of every order

**def make_order_in_progress(request, slug)**
********************************************
	Updates an order from active into in progress

**def make_order_done(request, slug)**
********************************************
	Updates an order from in progress into done	
	
**def view_done_orders(request)**
********************************************
	Gets all the done orders and passes them as argument to the view_done_orders.html page

**def bill_details(request, tid):**
********************************************
    Gets all the orders placed by a table and passes them as well as the total amount of the bill as argument to the bill_details.html

**def notifications(request, iden):**
********************************************
    Changes the status of order as done and passes the items that are ready to serve to the notifications.html

**def manage_shift(request, shift):**
********************************************
    Gets all the shifts of an employee and passes them as well as the total amount of the bill as argument to the shifts.html

**def dirty(request, table_id):**
********************************************
    Updates the table status as dirty and displays the success message
	
**def clear_bills(request, tid):**
********************************************
    Changes the status of OrderList to completed to indicate that the bill is not anymore active and displays the success message