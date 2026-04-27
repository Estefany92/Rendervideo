from flask import Flask
from utils.database import db
from flask_migrate import Migrate
import os

# Importar modelos ANTES de create_all()
from models.vendedor import Vendedor
from models.venta import Venta
from models.regla import Regla

app = Flask(__name__)

# Configuración PostgreSQL Render
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://rendervideo_db_user:gn3aPSDtiDcEtZiueU2OR2WSaDNAPiHt@dpg-d7neko1f9bms738fp97g-a/rendervideo_db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev')

# Inicializar base de datos
db.init_app(app)
migrate = Migrate(app, db)

# Registrar blueprints
from controllers.venta_controller import main_blueprint
app.register_blueprint(main_blueprint)

# Crear tablas automáticamente
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()