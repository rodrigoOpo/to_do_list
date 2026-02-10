import React from 'react'

const Card = ({title, content}) => {
  return (
    <>
    <div className='m-2 p-2 border-2xl rounded-2xl bg-blue-100 text-blue-800'>
        <h1>{title}</h1>
        <p>{content}</p>
    </div>
    </>
  )
}

export default Card