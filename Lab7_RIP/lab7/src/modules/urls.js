class Urls {
    constructor() {
        this.url = 'http://127.0.0.1:8000/';
    }

    stocks() {
        return `${this.url}doge/`
    }

    stock(id) {
        return `${this.url}doge/${id}/`
    }
}

export const urls = new Urls()