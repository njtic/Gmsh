# gmsh_generate_mesh.py
import gmsh
import sys
import matplotlib.pyplot as plt
import meshio


def generate_mesh(output_file):
    gmsh.initialize()
    # Создание точек
    p1 = gmsh.model.geo.addPoint(0, 0, 0)
    p2 = gmsh.model.geo.addPoint(1, 0, 0)
    p3 = gmsh.model.geo.addPoint(1, 1, 0)
    p4 = gmsh.model.geo.addPoint(0, 1, 0)

    # Создание линий
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)

    # Создание контурной петли из линий
    curveLoop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])

    # Использование контурной петли для создания плоской поверхности
    planeSurface = gmsh.model.geo.addPlaneSurface([curveLoop])

    # Синхронизация геометрии
    gmsh.model.geo.synchronize()

    # Генерация сетки для домена (необязательно)
    gmsh.model.mesh.generate(2)  # 2D сетка

    # Визуализация сетки (необязательно)
    #теперь выводится сразу график из matplotlib, а не открываетсяс gmsh
    #gmsh.fltk.run()

    gmsh.write("gmsh_test4.msh")
    # Creates graphical user interface
    mesh = meshio.read('gmsh_test4.msh')

    # Отображение данных с помощью matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=mesh.cells[0].data)
    plt.show()
    gmsh.finalize()

if __name__ == "__main__":
    output_file = sys.argv[1]
    generate_mesh(output_file)