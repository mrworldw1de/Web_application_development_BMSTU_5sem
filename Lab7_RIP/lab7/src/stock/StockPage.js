import {StockComponent} from "../components/stock/StockComponent.js";
import {BackButtonComponent} from "../components/back-button/BackButtonComponent.js";
import {MainPage} from "../pages/main/MainPage.js";
import {urls} from "../modules/urls.js";
import {ajax} from "../modules/ajax.js";



export class StockPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }
    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async getData() {
        return ajax.get(urls.stock(this.id))
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const backButton = new BackButtonComponent(this.page)
        backButton.render(this.clickBack.bind(this))

        const data = await this.getData()

        const stock = new StockComponent(this.page)
        stock.render(data.data)
    }

    get page() {
        return document.getElementById('stock-page')
    }

    getHTML() {
        return (
            `
                <div id="stock-page">
                </div>
            `
        )
    }

}