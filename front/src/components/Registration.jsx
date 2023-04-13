import {useState} from "react";
import ErrorMessage from "./ErrorMessage";

const Registration = () => {
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    const submitRegistration = async () => {
        const requestParams = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password,
                username: username
            })
        }

        const response = await fetch("/auth/register", requestParams);

        const data = await response.json();

        if (!data.id) {
            if (data.detail) {
                setErrorMessage(data.detail);
            } else {
                setErrorMessage("Неизвестная ошибка");
            };
        };
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password === confirmPassword && password.length > 5) {
            submitRegistration();
        } else {
            setErrorMessage("Убедитесь, что пароли совпадают и содержат более 5 символов")
        };
    };

    return (
        <div className="column">
            <form className="box" onSubmit={handleSubmit}>
                <h1 className="title has-text-centered">Регистрация</h1>
                <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="input" required></input>
                    </div>
                </div>

                <div className="field">
                    <label className="label">Логин</label>
                    <div className="control">
                        <input type="text" placeholder="Логин" value={username} onChange={(e) => setUsername(e.target.value)} className="input" required></input>
                    </div>
                </div>

                <div className="field">
                    <label className="label">Пароль</label>
                    <div className="control">
                        <input type="password" placeholder="Пароль" value={password} onChange={(e) => setPassword(e.target.value)} className="input" required></input>
                    </div>
                </div>
                <div className="field">
                    <label className="label">Подтверждение пароля</label>
                    <div className="control">
                        <input type="password" placeholder="Подтверждение пароля" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} className="input" required></input>
                    </div>
                </div>
                <ErrorMessage message={errorMessage} />
                <button className="button is-primary" type="submit">Регистрация</button>
            </form>
        </div>
    )
}

export default Registration;
