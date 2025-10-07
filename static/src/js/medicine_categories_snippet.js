/** @odoo-module */
import PublicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
import { renderToElement } from "@web/core/utils/render";

/**
 * Medicine Categories Widget
 */
var MedicineCategoriesWidget = PublicWidget.Widget.extend({
    selector: '.medicine_categories_snippet',

    willStart: async function () {
        // Fetch categories from your JSON route
        const data = await rpc('/medicine_categories', {});
        this.categories = data.categories || [];
    },

    start: function () {
        const refEl = this.$el.find("#medicine_categories_carousel");

        if (!this.categories || this.categories.length === 0) {
            refEl.html('<p class="text-center text-muted">No categories available</p>');
            return;
        }

        // Render the QWeb template with the categories
        const contentEl = renderToElement('my_ecommerce_website.medicine_categories_carousel_content', {
            categories: this.categories
        });

        refEl.empty().append(contentEl);
    }
});

// Register the widget
PublicWidget.registry.medicine_categories_snippet = MedicineCategoriesWidget;
export default MedicineCategoriesWidget;
