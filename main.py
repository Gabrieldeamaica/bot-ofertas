            time.sleep(2)
            
        return "Sucesso! 20 ofertas enviadas.", 200
    except Exception as e:
        return f"Erro: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
