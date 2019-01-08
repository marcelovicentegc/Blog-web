var camera, scene, renderer;
var geometry, material, mesh;

function init() {
    container = document.getElementById('pegafrito');

    camera = new THREE.PerspectiveCamera(75, container.clientWidth/container.clientHeight, 0.1, 10);
    camera.position.z = 1;

    scene = new THREE.Scene({
        autoUpdate: true
    })
    scene.background = new THREE.Color(0xffffff);
                    
    // TorusKnotGeometry looks nice
    // Background + diamond-like surface looks nice
    geometry = new THREE.SphereGeometry(.5, 15, 21);
    material = new THREE.MeshBasicMaterial({
        color: 0x000000, wireframe: true
    })
    mesh = new THREE.Mesh(geometry, material);
    scene.add(mesh);

    renderer = new THREE.WebGLRenderer({
        antialias: true
    });

    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);
        
};

function animate(time) {
    mesh.rotation.x = time * 0.0008;
    mesh.rotation.y = time * 0.0006;

    renderer.render(scene, camera);
    requestAnimationFrame(animate);
};

init();
requestAnimationFrame(animate);
            
window.addEventListener('resize', function () {
    renderer.setSize(container.clientWidth, container.clientHeight);
          camera.aspect = container.clientWidth / container.clientHeight;
          camera.updateProjectionMatrix();
});