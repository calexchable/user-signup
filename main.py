<!DOCTYPE html>
<html>
    <head>
        <style>
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>User Sign-up</h1>
        <form method="POST">
            <label for="username">Username:</label>
            <input name="username" type="text" value="" />
            <label for="password">Password:</label>
            <input name="password" type="password" value="" />
            <label for="verify">Verify Password:</label>
            <input for="verify" type="password" value="" />
            <label for="email">Email (optional):</label>
            <input for="email" type="text" value="" />
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>