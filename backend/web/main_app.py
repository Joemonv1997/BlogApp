from main_app_init import manageApp

app = manageApp()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
