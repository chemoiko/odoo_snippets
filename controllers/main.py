import time

from odoo import http
from odoo.http import request


class DynamicSnippets(http.Controller):
    """This class is for the getting values for dynamic product snippets"""

    @http.route("/top_selling_products", type="json", auth="public")
    def top_selling(self):
        """Function for getting the top sold products"""
        current_website = request.env["website"].sudo().get_current_website().id

        # New arrivals: newest published products first (SQL-orderable, simple & fast)
        products = (
            request.env["product.template"]
            .sudo()
            .search_read(
                [
                    ("is_published", "=", True),  # or ("website_published", "=", True)
                ],
                [
                    "id",
                    "name",
                    "image_1920",
                    "list_price",
                ],
                order="create_date desc",
                limit=4,
            )
        )

        unique_id = "pc-%d" % int(time.time() * 1000)

        # Return as dictionary instead of tuple
        return {
            "products": products,
            "categories": [],
            "website_id": current_website,
            "unique_id": unique_id,
        }

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
