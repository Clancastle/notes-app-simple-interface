from website import create_app  # import works.

app = create_app()

if __name__ == "__main__": #works on pycharm, not vscode
    app.run(debug=True)
