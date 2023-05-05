<script>
    import {request} from '../services/request.js'

    export default (await import('vue')).defineComponent({
        data(){
            return {
                colors: [
                    {color: 'Couleur', id: 0},
                    {color: 'rouge', id: 1},
                    {color: 'bleu', id: 2},

                ],
                selectedColor: 0,

                models: [],
                selectedModel: 0,

                manufacturers: [],
                manufacturersSelected: 0,

                categories: [],
                categorieSelected: 0,

                fueltype: [],
                fueltypeSelected: 0,

                engineVolume: [],
                engineVolumeSelected: 0,

                NbDoors: [],
                NbDoorsSelected: 0,

                driveWheel: [],
                driveWheelSelected: 0,

                gearBox: [],
                gearBoxSelected: 0,

                NbAirbags: [],
                NbAirbagsSelected: 0,

                cylinders: [],
                cylindersSelected: 0
            }
        },
        
        mounted(){
            this.loadFilters()
        },

        methods: {
            loadFilters: async function(){
                const response = await request('load-filters', 'GET', null)
                const json     = await response.json()

                this.initFilters(json)
            },

            initFilters: function(filters){
                this.colors     = filters.colors
                this.models     = filters.models
                this.NbAirbags  = filters.airbags
                this.cylinders  = filters.cylinders
                this.gearBox    = filters.gears_type
                this.NbDoors    = filters.doors
                this.categories = filters.categories
                this.fueltype   = filters.fuels_type
                this.driveWheel = filters.drive_wheels
                this.engineVolume  = filters.engines_volume
                this.manufacturers = filters.manufacturers 
            },

            makePredition: async function(){
                const response = await request('prediction', 'POST', {
                    test: 'test'
                }) 

                const json = await response.json()

                console.log(json);
            }
        }
    })
</script>

<template>
    <section id="filters-bar">
        <h3>Définiser les caractériques de votre voiture</h3>

        <div>
            <select v-model="manufacturersSelected" >
                <option v-for="manufacturer in manufacturers" :key="manufacturer" :value=manufacturer.id>{{ manufacturer.name }}</option>
            </select>

            <select v-model="selectedModel" >
                <option v-for="model in models" :key="model" :value=model.id>{{ model.model }}</option>
            </select>

            <select v-model="selectedColor" >
                <option v-for="color in colors" :key="color" :value=color.id>{{ color.color }}</option>
            </select>

            <select v-model="NbAirbagsSelected" >
                <option v-for="airbag in NbAirbags" :key="airbag" :value=airbag.id>{{ airbag.nb_airbag }}</option>
            </select>


            <select v-model="cylindersSelected" >
                <option v-for="cylinder in cylinders" :key="cylinder" :value=cylinder.id>{{ cylinder.nb_cylinder }}</option>
            </select>


            <select v-model="gearBoxSelected" >
                <option v-for="gear in gearBox" :key="gear" :value=gear.id>{{ gear.type }}</option>
            </select>

            <select v-model="NbDoorsSelected" >
                <option v-for="door in NbDoors" :key="door" :value=door.id>{{ door.nb_door }}</option>
            </select>

            <select v-model="categorieSelected" >
                <option v-for="categ in categories" :key="categ" :value=categ.id>{{ categ.categorie }}</option>
            </select>

            <select v-model="fueltypeSelected" >
                <option v-for="fuel in fueltype" :key="fuel" :value=fuel.id>{{ fuel.fuel }}</option>
            </select>

            <select v-model="engineVolumeSelected" >
                <option v-for="engine in engineVolume" :key="engine" :value=engine.id>{{ engine.engine_volume }}</option>
            </select>

            <select v-model="driveWheelSelected" >
                <option v-for="wheel in driveWheel" :key="wheel" :value=wheel.id>{{ wheel.type }}</option>
            </select>
        </div>

        <button @click="makePredition">
            Prédire le prix
        </button>
        
    </section>
</template>