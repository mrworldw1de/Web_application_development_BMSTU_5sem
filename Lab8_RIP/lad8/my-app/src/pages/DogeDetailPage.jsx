import React, {useEffect, useState} from "react";
import {useParams} from "react-router";
import {Table} from "react-bootstrap";
import Header from "../components/Header";
import GetDogeByPK from "../modules/GetDogeByPK";
function DogeDetailPage() {
    const pk = useParams().pk;
    console.log(pk);
    const [doge, setDoge] = useState({});
    const handleDoge = async () => {
        const result = await GetDogeByPK(pk);
        await setDoge(result);
    }
    useEffect(() => {
        handleDoge();}, []);
    useEffect(() => {
        console.log(doge);}, [doge])
    return (
        <div>
            <Header/>
            <Table striped bordered size="sm" className="fs-4">
                <tbody>
                <tr>
                    <td className="mx-2">Порода</td>
                    <td className="mx-2">{doge.dog_breed}</td>
                </tr>
                <tr>
                    <td className="mx-2">Имя собаки</td>
                    <td className="mx-2">{doge.dog_name}</td>
                </tr>
                <tr>
                    <td className="mx-2">Цена</td>
                    <td className="mx-2">{doge.price}</td>
                </tr>
                </tbody>
            </Table>

        </div>
    );
}
export default DogeDetailPage;