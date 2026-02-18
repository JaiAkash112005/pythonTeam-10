import { useNavigate } from "react-router-dom";

function Login(){
  const navigate = useNavigate();

  return(
    <div className="container mt-5 text-center">
      <h2>Campus Resource Management</h2>
      <button className="btn btn-primary mt-3"
        onClick={()=>navigate('/dashboard')}>
        Enter System
      </button>
    </div>
  );
}
export default Login;
