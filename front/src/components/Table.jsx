import React from 'react'
import {useSuspenseQuery} from '@tanstack/react-query'
import Card from './Card';

const Table = () => {

  const {data} = useSuspenseQuery({
    queryKey:["tasks"],
    queryFn:getTasks
  });

  return (
    <div className=' bg-blue-800'>
      <h1 className='text-blue-100'>TABLA DE TAREAS:</h1>
      {data.map(task => (
        <Card key={task.id} title={task.title} content={task.content}/>
      ))}
    </div>
  )
}

const getTasks = async () => {
  const response = await fetch("http://127.0.0.1:8000/tasks")
  return await response.json()
}

export default Table