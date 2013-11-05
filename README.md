This extension allows to quickly look up git info of running Flask webapp.

Use case: a tester can provide git info of running app by just looking at http://webapp-url/git
and see what current branch is, latest commit etc, whether work tree is dirty.

Typically, it's good to make sure whether the app was modified manually on server, and may be
see a few latest commits to understand how often the app has been updated lately and which
are the latest fixes/commits.

Usage:

<blockquote>
<code>
from flask.ext.gittest import gittest<br/>
 app.register_blueprint(gittest)
</code>
</blockquote>
