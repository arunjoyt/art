import frappe

def get_context(context):
    master_records = frappe.get_all("ART Artifact")
    art_display_items = []
    for record in master_records:
        doc = frappe.get_doc("ART Artifact", record.name).as_dict()
        art_display_items.append(doc)
    context.art_display_items = art_display_items
    return context