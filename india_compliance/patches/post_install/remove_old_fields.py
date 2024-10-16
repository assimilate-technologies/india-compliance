from india_compliance.gst_india.utils.custom_fields import delete_old_fields


def execute():
    delete_old_fields(
        "customer_gstin",
        (
            "Quotation",
            "Sales Order",
            "Delivery Note",
            "Sales Invoice",
            "POS Invoice",
        ),
    )

    delete_old_fields(
        ("reason_for_issuing_document", "ecommerce_gstin"), "Purchase Invoice"
    )
    delete_old_fields("pan_details", "Company")
    delete_old_fields("export_type", ("Customer", "Supplier"))
    delete_old_fields("company_address", "Journal Entry")
    delete_old_fields("reason_for_issuing_document", "Sales Invoice")

    # Field renamed post release
    delete_old_fields(
        ("custom_gst_breakup", "custom_gst_breakup_table"),
        (
            "Supplier Quotation",
            "Purchase Order",
            "Purchase Receipt",
            "Purchase Invoice",
            "Quotation",
            "Sales Order",
            "Delivery Note",
            "Sales Invoice",
            "POS Invoice",
        ),
    )
