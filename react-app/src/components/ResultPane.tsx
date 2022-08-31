import React from "react";
import '../styles/resultpane.css';

export default function ResultPane() {
    return (
        <div className="resultpane">
            <ListingContainer>
                {/* just for testing purposes */}
                <Listing
                    img="https://images.familyhomeplans.com/cdn-cgi/image/fit=scale-down,quality=85/plans/41438/41438-b580.jpg"
                    price="2000"
                    address="1800 Rando Street"
                    platform="zillow"
                    url="https://www.zillow.com/?utm_medium=cpc&utm_source=google&utm_content=1471764169|65545421228|aud-1414479055879:kwd-570802407|517438046043|&semQue=null&gclid=CjwKCAjw6raYBhB7EiwABge5KoZL19DnLxot3HYfMQFe0AiakDIlE8Rg_G_MT5ylxpc57YpnioX4txoCrFwQAvD_BwE"
                    beds="4"
                    baths="2"
                    area="800"
                >
                </Listing>
                <Listing
                    img="https://wp-tid.zillowstatic.com/25/ZG_BrandGTM_0321_GettyImages-528689860-RT-ed6165.jpg"
                    price="800"
                    address="2000 Rando Street St Pauls, WA 980342"
                    platform="zillow"
                    url="https://wp-tid.zillowstatic.com/25/ZG_BrandGTM_0321_GettyImages-528689860-RT-ed6165.jpg"
                    beds="4"
                    baths="2"
                    area="800"
                >
                </Listing>
            </ListingContainer>
        </div>
    )
}

function ListingContainer(props: any) {
    return (
        <div className="listing-container">
            {props.children}
        </div>
    )
}

function Listing(props: any) {
    // address, price, beds, baths, sqft area, url, image, coords, platform
    //  const {img, price, address} = [props.img, props.price, props.address];
    return (
        <div className="listing">
            <img className="listing-image" src={props.img} alt="property"></img>
            <div className="listing-text">
                <p>${props.price}</p>
                <p>{props.address}</p>
                <p>
                    {props.beds} beds {props.baths} baths | {props.area} sqft
                </p>
                <a href={props.url} target="_blank" rel="noreferrer" className="button">See on {props.platform}</a>
            </div>
        </div>
    )
}