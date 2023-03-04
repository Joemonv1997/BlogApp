import React from 'react';

export const homePage=async()=>{
    const request= await fetch("http://127.0.0.1:5500")
    const response =await request.json()
    console.log(response);
    if (response.code==200){
        return response.data["hello"]
    }
    else{
        throw new Error("Fetching Unsuccessfull")
    }
    
}
    