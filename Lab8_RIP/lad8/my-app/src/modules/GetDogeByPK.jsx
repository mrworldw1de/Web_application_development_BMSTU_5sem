const GetDogeByPK = async (pk = 1) => {
    return await fetch(`http://127.0.0.1:8000/doge/${pk}/`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetDogeByPK;