import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import * as businessActions from '../../store/business';
import noImage from "../../images/no-image.png"
import './Business.css';
import LoadingAnimation from "../Loading";


function BusinessMainPage() {
    const dispatch = useDispatch();
    const businesses = useSelector(state => state.business.list);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        const loadingTimeout = setTimeout(() => {
            setLoading(false);
            dispatch(businessActions.getAllBusinesses());
        }, 100);

        return () => clearTimeout(loadingTimeout);
    }, [dispatch]);

    let getPrev = (business) => {
        let res
        if (business.images.length) {
            let arr = business.images
            arr.forEach((bus) => {
                if (bus.image_preview) {
                    res = bus.image_url
                }
            })
        } else {
            res = noImage
        }
        return res
    }

    if (loading) {
        return <LoadingAnimation />;
    }

    return (
        <div className='businessMain__grid'>
            {businesses && businesses.map((business) => (
                <div key={business.id} className='businessMain__item'>
                    <div className="businessMain__image">
                        <img src={getPrev(business)}
                            className='busImg'
                            alt={business.name}
                            key={business.id}
                        />
                    </div>
                    <p className="businessMain_name">{business.name}</p>
                    <p>Category: {business.category}</p>
                    <p>Rating: {business.avg_rating}</p>
                    <p>{business.address}, {business.city}, {business.state} {business.zip_code}</p>
                    <p>{business.phone_number}</p>
                    <Link to={`/business/${business.id}`}>View More</Link>
                </div>
            ))}
        </div>
    );
}

export default BusinessMainPage;
