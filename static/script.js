const testFunction = () => {
    let inputValue = document.getElementById(" input").value;
    console.log(inputValue);
    return inputValue;
}
document.addEventListener('DOMContentLoaded', function () {
    var calculate = function () {
        fetch('/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                inputstring: testFunction()
            }),
        }).then(
            function (response) {
                console.log(response)
                return response.json()
            }).then(
                function (data) {
                    document.getElementById('result').innerText = data;
                }).catch(function () { });
    };

    // document.getElementById('calculate').onclick = function (event) { calculate(); return false; };
    document.getElementById(' input').onkeyup = (event) => calculate();
});