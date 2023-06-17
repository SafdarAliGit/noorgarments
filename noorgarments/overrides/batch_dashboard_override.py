from frappe import _


def get_data():
	return {
		"fieldname": "batch_id",
		"transactions": [
			{"label": _("Buy"), "items": ["Purchase Invoice"]},
		],

	}
