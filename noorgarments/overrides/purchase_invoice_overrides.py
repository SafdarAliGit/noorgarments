import frappe
from frappe import flags
from erpnext.accounts.doctype.purchase_invoice.purchase_invoice import PurchaseInvoice


class PurchaseInvoiceOverrides(PurchaseInvoice):
    def __init__(self, *args, **kwargs):
        super(PurchaseInvoice, self).__init__(*args, **kwargs)

    def on_submit(self):
        items = frappe.get_all("Purchase Invoice Item",
                               filters={"parent": self.name},
                               fields=["item_code", "batch_id", "qty", "name"])
        for item in items:
            if item.batch_id:
                pii = frappe.get_doc("Purchase Invoice Item", item.name)
                pii.batch_no = item.batch_id
                pii.flags.ignore_validate_update_after_submit = True
                pii.insert()
    def on_submit(self):
        super(PurchaseInvoice, self).on_submit()
        items = frappe.get_all("Purchase Invoice Item",
                               filters={"parent": self.name},
                               fields=["item_code", "batch_id", "qty", "name"])

        for item in items:
            if item.batch_id:
                batch = frappe.new_doc(doctype="Batch")
                batch.batch_id = item.batch_id
                batch.item = item.item_code
                batch.batch_qty = item.qty
                batch.insert()





