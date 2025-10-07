import time

from odoo import http
from odoo.http import request


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

    @http.route("/medicine_categories", type="json", auth="public")
    def medicine_categories(self):
        """Return the latest 4 product.category records by create_date."""
        categories = (
            request.env["product.category"]
            .sudo()
            .search_read(
                [],
                ["id", "name"],
                order="create_date desc",
                limit=4,
            )
        )

        return {"categories": categories}
