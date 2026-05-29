# middleware/error_handler.py

from flask import jsonify
import traceback


def register_error_handlers(app):

    # 404 Error
    @app.errorhandler(404)
    def not_found_error(error):

        return jsonify({

            "success": False,

            "message":
            "Resource Not Found",

            "error":
            str(error)

        }), 404

    # 500 Error
    @app.errorhandler(500)
    def internal_server_error(error):

        return jsonify({

            "success": False,

            "message":
            "Internal Server Error",

            "error":
            str(error)

        }), 500

    # Generic Exception Handler
    @app.errorhandler(Exception)
    def handle_exception(error):

        traceback.print_exc()

        return jsonify({

            "success": False,

            "message":
            "An Unexpected Error Occurred",

            "error":
            str(error)

        }), 500