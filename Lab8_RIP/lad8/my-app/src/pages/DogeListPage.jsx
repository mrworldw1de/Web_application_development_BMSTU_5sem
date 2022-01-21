import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Header from "../components/Header";
import GetDoges from "../modules/GetDoges.jsx";

function DogeListPage() {
    const [Doges, setDoges] = useState([]);
    const handleDogesList = async () => {
        const results = await GetDoges();
        await setDoges(results);
    }
    useEffect(() => {
        handleDogesList();
    }, []);
    return (
        <div>
            <Header/>
            <ul className="fs-4">
                {Doges.map((doge) => {
                    return (
                        <li key={doge.pk}><Link to={"/doge/" + doge.pk.toString()}
                                                     className="text-decoration-none link-dark">
                        {doge.dog_breed}</Link></li>);

                })}
            </ul>
         </div>
    );
}
export default DogeListPage;