import React from 'react'
import { useLoaderData } from 'react-router-dom';

function Home() {
  const data=useLoaderData();
  return (
    <div>
      <h1>Home Page</h1>
      <h2>{data}</h2>
    </div>
  )
}

export default Home
