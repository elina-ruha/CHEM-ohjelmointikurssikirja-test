import os

def setup(app):
    def create_static_dir(app):
        static_dir = os.path.join(app.outdir, '_static')
        os.makedirs(static_dir, exist_ok=True)
    
    app.connect('builder-inited', create_static_dir)
    return {'version': '0.1'}
