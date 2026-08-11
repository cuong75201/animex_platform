import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { QueryCache, QueryClient, QueryClientProvider } from "@tanstack/react-query"
import './index.css'

const handleApiError = (error:Error) => {
  if (error)
}

const queryClient=new QueryClient({
  queryCache= new QueryCache()
})
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>

    </QueryClientProvider>
  </StrictMode>,
)
