# Collect website user activity data and index to file or HEC

Adapted from https://github.com/oizmerly/dejavu

## Usage

```
pip install -r requirements.txt
flask run 
```
 * Open a browser at http://127.0.0.1:5000/
 


For the sake of simplicity only `mousedown` and `mouseup` events are handled in our browser client. Adding more event handlers is very simple. For instance one may trap `mousemove` events using the code below:

```js
    document.addEventListener('mousemove', function(event) {
        postEventToSplunk({
            type: event.type,
            info: {
                x: event.x,
                y: event.y,
                button: event.buttons != undefined ? event.buttons : event.which
            }
        });
    });
```

Splunk HTTP event collector supports "batching" (i.e., merge multiple pieces of input data into a single chunk). It's strongly recommended to use batching for `mousemove` because it produces huge number of individual events.

Due to restrictions of cross-site scripting limitations it's less convenient to send data to Splunk server directly. Instead javascript code posts events to a "proxy" located on the same server. `agent/dejavu.php` is our simple proxy that resends it's input to Splunk server.

In our tictactoy demo every gameboard cell has its own `id` that is composed of cell column and row. Browser agent traps user clicks and they immediately become available in Splunk in form of json entities. For example click in the middle of the gameboard is indexed as:

```json
{
  "type": "mousedown",
  "info": {
    "x": 138,
    "y": 136,
    "target": {
      "id": "(1,1)",
      "class": "class: (1,1)"
    }
  }
}
```

## License
The MIT License (MIT)

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
