import frappe


@frappe.whitelist()
def fetch_recent_soled_items(**args):
    item_code = args.get('item_code')
    data = {}
    data['sales_history'] = frappe.db.sql(
        """
        select 
            `tabSales Invoice Item`.name, `tabSales Invoice Item`.parent,
            `tabSales Invoice`.posting_date,`tabSales Invoice`.customer_name,
            `tabSales Invoice Item`.item_code,`tabSales Invoice Item`.`item_name`,
            `tabSales Invoice Item`.rate
        from `tabSales Invoice`, `tabSales Invoice Item`
        where `tabSales Invoice`.name = `tabSales Invoice Item`.parent
            and `tabSales Invoice`.docstatus = 1 and `tabSales Invoice Item`.item_code = %s  order by `tabSales Invoice Item`.parent 
        """,(item_code, ),
        as_dict=1
    )[:5]

    data['purchase_history'] = frappe.db.sql(
        """
        select 
            `tabPurchase Invoice Item`.name, `tabPurchase Invoice Item`.parent,
            `tabPurchase Invoice`.posting_date,`tabPurchase Invoice`.supplier_name,
            `tabPurchase Invoice Item`.item_code,`tabPurchase Invoice Item`.`item_name`,
            `tabPurchase Invoice Item`.rate
        from `tabPurchase Invoice`, `tabPurchase Invoice Item`
        where `tabPurchase Invoice`.name = `tabPurchase Invoice Item`.parent
            and `tabPurchase Invoice`.docstatus = 1 and `tabPurchase Invoice Item`.item_code = %s  order by `tabPurchase Invoice Item`.parent 
        """, (item_code,),
        as_dict=1
    )[:5]
    return data

@frappe.whitelist()
def fetch_recent_purchased_items(**args):
    item_code = args.get('item_code')
    data = frappe.db.sql(
        """
        select 
            `tabPurchase Invoice Item`.name, `tabPurchase Invoice Item`.parent,
            `tabPurchase Invoice`.posting_date,`tabPurchase Invoice`.supplier_name,
            `tabPurchase Invoice Item`.item_code,`tabPurchase Invoice Item`.`item_name`,
            `tabPurchase Invoice Item`.rate
        from `tabPurchase Invoice`, `tabPurchase Invoice Item`
        where `tabPurchase Invoice`.name = `tabPurchase Invoice Item`.parent
            and `tabPurchase Invoice`.docstatus = 1 and `tabPurchase Invoice Item`.item_code = %s  order by `tabPurchase Invoice Item`.parent 
        """, (item_code,),
        as_dict=1
    )[:5]
    return data

