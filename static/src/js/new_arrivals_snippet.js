/** @odoo-module */
import PublicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
import { renderToElement } from "@web/core/utils/render";

export function _chunk(array, size) {
    const result = [];
    for (let i = 0; i < array.length; i += size) {
        result.push(array.slice(i, i + size));
    }
    return result;
}

var NewArrivalsWidget = PublicWidget.Widget.extend({
    selector: '.new__arrivals_product_snippet',

    willStart: async function () {
        const data = await rpc('/new_arrivals', {});
        this.products = data.products || [];
        this.categories = data.categories || [];
        this.website_id = data.website_id;
        this.unique_id = data.unique_id;
    },

    start: function () {
        const { products } = this;



        const chunkData = _chunk(products, 4);

        const contentEl = renderToElement('my_ecommerce_website.products_carousel_content', {
            products: products,
            chunkData: chunkData
        });
        refEl.empty().append(contentEl);
    }
});

PublicWidget.registry.new_arrivals_snippet = NewArrivalsWidget;
export default NewArrivalsWidget;


