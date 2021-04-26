Billing
=======

With the billing module you can create quotes, orders and invoices. The documents 
can either be printed or you can send them by e-mail as a PDF attachment. You 
can also enter your expenses. With the report tool you can easily see your income 
and expenses. You can create as many books as you want and you can call them 
whatever you like.

The billing module supports:

- :ref:`links`
- :ref:`custom-fields`
- :ref:`comments`
- :ref:`sharing`
- :ref:`files`

.. figure:: /_static/using/billing/billing-module.png
   :width: 100%

   Billing module

Languages
---------

The billing module is multilingual. If you're going to use more than one 
language is best that you start with configuring these because then you can 
input all translations directly when configuring statuses, products and 
templates.

Enter the languages at:

Administration -> Languages

Book properties
---------------

The books contain invoices, quotes or orders. Per book you can configure things 
like tax, order numbers, statuses and templates. You can set the following book 
properties:

.. figure:: /_static/using/billing/book-properties.png
   :width: 100%

   Book dialog

+---------------------------+--------------------------------------------------+
| Property                  | Description                                      |               
+===========================+==================================================+
| Name                      | The name of the book                             |
+---------------------------+--------------------------------------------------+
| Order prefix              | The prefix of order numbers.                     |                     
+---------------------------+--------------------------------------------------+                                          
| Order no. length          | The length of the number. eg. 1 becomes 00001 if |
|                           | this is set to 5.                                |                                          
+---------------------------+--------------------------------------------------+
| Last ID                   | The last ID used for an invoice number. You can  |
|                           | change this in case you want to start with a     |
|                           | higher number                                    |
+---------------------------+--------------------------------------------------+
| Tax.                      | The default Tax percentage you apply to invoice  |
|                           | items.                                           |
+---------------------------+--------------------------------------------------+
| Currency                  | The currency symbol                              |
+---------------------------+--------------------------------------------------+
| Country                   | The country of the company. This is important for| 
|                           | tax calculations in the European Union.          |
+---------------------------+--------------------------------------------------+
| BCC                       | A copy of all e-mails sent to customers will be  |
|                           | sent to this address.                            |
+---------------------------+--------------------------------------------------+
| E-mail address            | By default the Group-Office webmaster email      |
|                           | address will be used. Override that here.        |
+---------------------------+--------------------------------------------------+
| E-mail name               | By default the Group-Office title will be used.  |
|                           | Override that here.                              |
+---------------------------+--------------------------------------------------+
| Call after days           | When you set a number here a task will be created| 
|                           | after x days to remind you with a call.          |
+---------------------------+--------------------------------------------------+
| Allow deletion of items   | Check to prevent deleting of items even by       |
|                           | administrators.                                  |
+---------------------------+--------------------------------------------------+
| Use fixed address book    | Limit customer selection to this address book.   |
+---------------------------+--------------------------------------------------+

Order ID prefix
```````````````

By default GO creates a number like Q200900001 for a quote and I200900001 for an invoice. 

The following automatic tags can be used:

- %y will be replaced by the full 4 digit year.
- %m will be replaced by the 2 digit month number
- %r will be replaced by a random digit between 0 and 9. This variable can be used multiple times.
- {autoid} will be replaced by the automatic generated id in the database. When not used the ID is appended to the number.


PDF templates
`````````````

Here you can setup templates for the invoice, quotes or PDF documents. You can change your address details and setup the invoice items table here.

PDF templates also support a background image or base PDF to use as stationery paper.

:download:`Download an example PDF document </_static/using/billing/Sample_invoice.pdf>`

The variables you can use in the fields of the template is identical to the template syntax of :ref:`e-mail templates <template-variables>`.


Creating a custom PDF script
++++++++++++++++++++++++++++

Sometimes the default PDF does not suit your needs. In that case you can program 
your own PDF creator script. All you need to do is copy modules/billing/Pdf.php a
nd put the path to the new file in :ref:`config.php <configuration>` like this:

````````````````````````````````````````````````````````
$config['billing_pdf_class'] = '/any/path/to/Pdf.php'; 
````````````````````````````````````````````````````````

ODF Templates
`````````````

You can also create ODF templates for invoice items. The benefit is that you can edit the documents after generation.

You can also create odt templates so that you can edit invoices after creating them. You can use the same variables as for e-mail templates.  

:download:`Download an example ODF document </_static/using/billing/Sample_invoice.odt>`

Statuses
--------

Order statuses need to be setup as well. Of course status determine the state of 
the invoice or quote, but it also determines the layout of the invoice document a
nd the e-mail message to the customer.

On the status properties you have the following options:

+---------------------------+--------------------------------------------------+
| Property                  | Description                                      |                                                                                     
+===========================+==================================================+
| Name                      | The name of the status (for each language).      |
+---------------------------+--------------------------------------------------+
| PDF template              | The PDF template for this status                 |
+---------------------------+--------------------------------------------------+
| ODF template              | The ODF template for this status                 |   
+---------------------------+--------------------------------------------------+
| E-mail template           | The e-mail template for this status              |                                          
+---------------------------+--------------------------------------------------+
| Required status           | If you set status here, the invoice can only get |
|                           | this status when it has this required status in  |
|                           | it's history.                                    |
+---------------------------+--------------------------------------------------+
| Max order age             | When the invoice is older than this age it will  |
|                           | turn red in the invoice grid.                    |
+---------------------------+--------------------------------------------------+
| Order is not paid in this | For automatically setting the payment date when  |
| status                    | the status changes                               |
+---------------------------+--------------------------------------------------+
| Remove from stock         | Decrease the product stock when this status is   |
|                           | set                                              |
+---------------------------+--------------------------------------------------+
| Make order read only      | Nobody can change this invoice when you check    |
|                           | this                                             |
+---------------------------+--------------------------------------------------+
| Color                     | Color used in the grid                           |
+---------------------------+--------------------------------------------------+
| Bill extra item           | You can automatically add a new item to the      |
|                           | invoice when you set this status. For example    |
|                           | extra costs when it's over due                   |
+---------------------------+--------------------------------------------------+

Permissions
```````````

If you don't want to allow anyone to set this status. You can configure that here.


E-mail templates
````````````````

In the e-mail template per status you can use the following variables:

Order data
++++++++++

- {company_id}		 The company id
- {contact_id}		 The contact id
- {id}		         The database id of the order
- {order_id}		 The textual order ID
- {po_id}			 The purchase order ID
- {btime}			 The date of the order
- {due_date}		Due date for payment
- {due_days}		Days left for payment
- {dtime)		Delivery date
- {reference}		 The order reference
- {total}			 The gross amount of the order 
- {subtotal}		 The nett amount of the order
- {vat}
- {total_paid}          Amount paid
- {total_outstanding}   Amount outstanding (Since 6.4.75)

Custom fields
+++++++++++++

Lookup the database name in the custom fields module and use {order:databaseName}.

Customer
++++++++

- {customer_salutation}
- {customer_name}
- {customer_address}
- {customer_address_no}
- {customer_zip}
- {customer_city}
- {customer_state}
- {customer_vat_no}
- {customer_country}
- {customer_countryname} 

Logged in user
++++++++++++++

For the logged in user fields see this page: :ref:`template-variables`

Invoice items
+++++++++++++

You can generate a table of the invoice items like this::

	{items_table_start}
	<table style="width: 100%;">
	<tbody>
			 <tr>
					<td><strong>Description</strong></td>
					<td style="text-align: center;"><strong>Amount</strong></td>
					<td style="text-align: right;"><strong>Unit price</strong></td>
					<td style="text-align: right;"><strong>Price</strong></td>
			</tr>
			<tr>
					<td>{item_description}</td>
					<td style="text-align: center;">{item_amount}</td>
					<td style="text-align: right;">{item_unit_price}</td>
					<td style="text-align: right;">{item_total}</td>
			</tr>
			<tr>
					<td colspan="3" style="font-weight: bold;"><br />
					Totaal (including VAT):</td>
					<td style="border-top: 1px solid black; font-weight: bold; text-align: right;"><br />
					&euro; {order_total}</td>
			</tr>
	</tbody>
	</table>




Invoice item rows in ODF templates
++++++++++++++++++++++++++++++++++

You can use these tags in item rows::

	{amount_delivered}
	{markup}
	{cost_code}
	{discount}
	{vat} VAT Percentage. eg. 19 for 19%
	{amount}
	{unit_total} The unit price including VAT.
	{unit_list} The unit price from the catalog.
	{unit_price} The unit price without VAT
	{unit_cost} The unit cost price without VAT
	{description}
	{item_total} The localized item total (amount*unit_total) incl. VAT
	{item_subtotal} The localized item total (amount*unit_price) excl. VAT

Cost codes
----------

Cost codes can be set per invoice row. They can be exported with a report for the accountant.


Purchase order books
--------------------

Purchase order book makes it behave a different. It enables a "Stock" button where you can purchase new items for products in your catalog. It queries the products that are lower in stock than the minimum stock value of the product. When you order these items it will generate purchase orders for the product suppliers.

It will also enable deliveries in the purchase orders so you can keep track of how many items have been delivered to you.


Custom fields
-------------

You can use custom fields for orders. There's one special thing to note. When you select a customer from the address book all fields with matching database names will be copied to the invoice.

.. note:: The match used to be made on the field label. Since 6.4 the match is made by database name.
