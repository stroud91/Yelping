import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import * as businessActions from "../../store/business";
import * as imageActions from "../../store/images";
import "../Bussiness/Business.css";
import MainPage from "../MainPageView";
import noImage from "../../images/no-image.png"
import { searchBusinessByName } from "../../store/business";
import LoadingAnimation from "../Loading";

function QueryBusiness() {
  const dispatch = useDispatch();
  let businesses = useSelector((state) => state.business.search);

  businesses = businesses["queried businesses"];


  useEffect(() => {
    dispatch(searchBusinessByName());
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


  if(!businesses){
    return <LoadingAnimation />
  }
  return (
    <div>
      {businesses.length === 0 ? (
        <div>
          <p> No restaurants found. Please try a different search.</p>
          <Link to="/">
            <button className="noResultButton">Go back to main page</button>
          </Link>
        </div>
      ) : (

        <ul className="businessMain__grid">
          {businesses &&
            businesses.map((business) => (
              <li key={business.id} className="businessMain__item">
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
                <p>
                  {business.address}, {business.city}, {business.state}{" "}
                  {business.zip_code}
                </p>
                <p>{business.phone_number}</p>
                <Link to={`/business/${business.id} `}>View More</Link>
              </li>
            ))}
        </ul>
      )}
    </div>
  );
}

export default QueryBusiness;
