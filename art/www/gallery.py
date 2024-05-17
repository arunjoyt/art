import frappe

def get_context(context):
    master_records = frappe.get_all("ART Artifact")
    art_display_items = []
    for record in master_records:
        doc = frappe.get_doc("ART Artifact", record.name).as_dict()
        art_display_items.append(doc)
    context.art_display_items = art_display_items
    # if caching is enabled, new Aritfacts added won't be displayed on webpage unless cache is cleared.
    # this happens only in prodoction, works fine in developemnt even when cache is enabled.
    context.no_cache = 1
    return context