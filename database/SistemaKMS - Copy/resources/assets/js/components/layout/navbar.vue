<template>
    <!-- Navbar -->
    <nav class="main-header navbar navbar-expand navbar-white navbar-light">
        <!-- Left navbar links -->
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
            </li>
            <li class="nav-item d-none d-sm-inline-block">
                <router-link to="/contacto" class="nav-link"> Contacto </router-link>
            </li>
            <li class="nav-item d-none d-sm-inline-block">
                <a href="https://gestion-de-conocimiento.github.io/" target="_blank" class="nav-link">Documentación</a>
            </li>
        </ul>

        <!-- Right navbar links -->
        <ul class="navbar-nav ml-auto">
            <!-- Navbar Search -->



            <!-- Notifications Dropdown Menu -->
            <li class="nav-item dropdown">
                <a class="nav-link" data-toggle="dropdown" href="#">
                    <i class="fas fa-chevron-circle-down"></i>

                </a>
                <div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">



                    <router-link to="/perfil" class="dropdown-item">
                        <i class="fas fa-user-alt mr-2"></i> Perfil
                        <span class="float-right text-muted text-sm"></span>
                    </router-link>

                    <div class="dropdown-divider"></div>
                    <a href="/logout" class="dropdown-item">
                        <i class="fas fa-sign-out-alt mr-2"></i> Cerrar sesión
                        <span class="float-right text-muted text-sm"></span>
                    </a>

                </div>
            </li>
            <li class="nav-item">
                <a class="nav-link" data-widget="fullscreen" href="#" role="button">
                    <i class="fas fa-expand-arrows-alt"></i>
                </a>
            </li>

        </ul>
    </nav>
    <!-- /.navbar -->
</template>
<script>
    export default {

    };

</script>
