from odoo import http
from odoo.http import request
import json


class DynamicSnippets(http.Controller):
    """This class is for the getting values for dynamic product snippets"""

    @http.route("/new_arrivals", type="json", auth="public")
    def top_selling(self):
        """Return filtered top-level product categories"""
        keywords = ["antibiotic", "cold", "pain", "vitamin"]
        print("=== /top_selling_products called ===")
        print(f"Keywords for filtering: {keywords}")
        all_categories = (
            request.env["product.category"]
            .sudo()
            .search_read(
                [("parent_id", "=", False)],
                ["id", "name"],
                order="name",
            )
        )

        filtered_categories = [
            cat
            for cat in all_categories
            if any(keyword.lower() in cat["name"].lower() for keyword in keywords)
        ]

        return {"categories": filtered_categories}

    @http.route("/get_medicine_categories", auth="public", type="json", website=True)
    def get_medicine_categories(self):
        """Return all product public categories (id and name) in descending order."""
        public_categs = (
            request.env["product.public.category"]
            .sudo()
            .search_read(
                [],  # no filter, get all categories
                ["id", "name"],  # only id and name
                order="id desc",  # descending order by ID
                limit=4,  # only latest 4
            )
        )
        return {"categories": public_categs}
