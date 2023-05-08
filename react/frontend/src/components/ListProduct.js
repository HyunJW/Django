import React, { useRef, useEffect, useState } from "react";
import './main.css';
import { useNavigate } from "react-router";
import ProductItem from "./ProductItem";

function ListProduct(){
    const navigate = useNavigate();
    const [items, setProductList] = useState([]);
    function getList(url){
        fetch('http://localhost' + url)
            .then(response => { return response.json(); })
            .then(data => { setProductList(data); });
    }
    useEffect(() => { getList('/list'); }, []);
    return (
        <>
            <h2>상품목록</h2>
            <button onClick={() => navigate('/write')}>상품등록</button>
            <hr />
            등록된 상품수: {items.length}
            <br /><br />
            <div style={{
                display: 'grid',
                gridTemplateRows: '1fr',
                gridTemplateColumns: '1fr 1fr 1fr 1fr 1fr',
            }}>
                {items.map(
                    ({ product_code, product_name, price, filename }) =>
                    (<ProductItem
                        product_code={product_code}
                        product_name={product_name}
                        price={price}
                        filename={filename}
                        key={product_code}
                        />
                    )
                )}
            </div>
        </>
    );
};
export default ListProduct;