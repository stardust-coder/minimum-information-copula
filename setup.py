import os
from setuptools import setup, find_packages

# パッケージ名
NAME = 'MIC'
 
# バージョンの読み込み
setup_dir = os.path.abspath(os.path.dirname(__file__))
ver = {}
with open(os.path.join(setup_dir, NAME, '__version__.py')) as f:
    exec(f.read(), ver)
 
def _requires_from_file(filename):
    return open(filename).read().splitlines()
 
setup(
    # パッケージ名
    name=NAME,
    # パッケージの説明
    description='dependence modeling using minimum information copula',
    # バージョン
    version=ver.get('__version__'),
    # インストールするパッケージ
    packages=find_packages(),
    # ソースファル以外のパッケージに含めるファイル
    #package_data={NAME: ['readme.txt']},
    include_package_data=True,
    # 必要なPythonのバージョン
    python_requires='>=3.7',
    # 必要なライブラリなど
    install_requires=_requires_from_file('requirements.txt'),
)

