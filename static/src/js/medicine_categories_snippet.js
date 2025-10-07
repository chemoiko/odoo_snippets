/** @odoo-module **/
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.medicine_categories = publicWidget.Widget.extend({
    selector: '.medicine_categories_snippet',
    async willStart() {
        // Fetch categories from JSON route
        const result = await rpc('/get_medicine_categories', {});
        console.log('Fetched medicine categories:', result);


        if (result) {
            // Render the QWeb template and inject into the widget container
            this.$target.empty().html(
                renderToElement(
                    'my_ecommerce_website.medicine_categories_carousel_content',
                    { result: result }
                )
            );
        }
    },
});
