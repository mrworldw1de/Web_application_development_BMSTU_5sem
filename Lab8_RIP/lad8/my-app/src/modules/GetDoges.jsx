const GetDoges = async () => {
    return await fetch(`http://127.0.0.1:8000/doge/`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetDoges;