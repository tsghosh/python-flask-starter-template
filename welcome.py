#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify
from flask_restful import Api
from controllers.welcome.welcomeController import WelcomeController

app = Flask(__name__)

api = Api(app)

api.add_resource(WelcomeController, '/api/welcome');

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='127.0.0.1', port=int(port))
