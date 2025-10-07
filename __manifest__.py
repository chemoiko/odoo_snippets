{
    "name": "My E-commerce Snippets",
    "version": "1.0",
    "category": "Website",
    "summary": "Custom snippets for an e-commerce site",
    "depends": ["website_sale"],  # depend on e-commerce module
    "data": [
        "views/snippets/static_template.xml",
        "views/snippets/new_arrivals_initializer.xml",
        "views/snippets/medicine_categories_initializer.xml",
        "views/snippets/campaigns_carousel_initializer.xml",
        "views/snippets/trusted_brands_initializer.xml",
        "views/snippets/snippets.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "my_ecommerce_website/static/src/js/new_arrivals_snippet.js",
            "my_ecommerce_website/static/src/xml/new_arrivals_snippet_templates.xml",
            "my_ecommerce_website/static/src/xml/medicine_categories_snippet_templates.xml",
            "my_ecommerce_website/static/src/js/new_arrivals_snippet.js",
            "my_ecommerce_website/static/src/js/medicine_categories_snippet.js",
        ],
    },
    "installable": True,
    "application": True,
}
