export class StockComponent {
    constructor(parent) {
        this.parent = parent
    }
    getHTML(data) {
        return (
            `
                <div class="card mb-3" style="width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${data["dog_breed"]}</h5>
                                <h7 class="card-title">Имя: ${data["dog_name"]}</h7>
                                <p class="card-text">${data["price"]}$</p>
                            </div>
                        </div>
                    </div>
                </div>
            `
        )
    }
    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
    }
}