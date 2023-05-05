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
                manufacturersSelected: 0,

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

                NbAibags: [],
                NbAibagsSelected: 0,

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
                this.colors = filters.colors
            }   
        }
    })
</script>

<template>
    <section id="filters-bar">
        <h3>Définiser les caractériques de votre voiture</h3>

        <div>

            <select v-model="selectedModel" >
                <option v-for="model in models" :key="model" :value=model.id>{{ model.color }}</option>
            </select>

            <select v-model="selectedColor" >
                <option v-for="color in colors" :key="color" :value=color.id>{{ color.color }}</option>
            </select>

        </div>

    </section>
</template>